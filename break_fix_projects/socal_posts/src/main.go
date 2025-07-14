package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	_ "github.com/mattn/go-sqlite3"
)

type Post struct {
	PostID   int    `json:"post_id"`
	PostType string `json:"post_type"`
	Comments int    `json:"comments"`
	Likes    int    `json:"likes"`
}

func main() {
	// Configuration
	dbPath := "../database/social_posts.db"
	// Define the path for the output JSON file.
	jsonOutputPath := "../data/posts.json"

	// Check if the database file exists
	if _, err := os.Stat(dbPath); os.IsNotExist(err) {
		log.Fatalf("Database file not found at %s. Please ensure the path is correct and the database has been created.", dbPath)
	}

	// Connect to the SQLite database
	db, err := sql.Open("sqlite3", dbPath)
	if err != nil {
		log.Fatalf("Failed to open database connection: %v", err)
	}

	defer db.Close()

	if err := db.Ping(); err != nil {
		log.Fatalf("Failed to connect to the database: %v", err)
	}

	fmt.Printf("Successfully connected to the database: %s\n", dbPath)

	// Define and execute the SQL query with JOINs
	query := `
		SELECT
				pt.Post_id,
				pt.Post_Type,
				pc.comments,
				pl.likes
		FROM
				Post_Types AS pt
		LEFT JOIN Post_Comments AS pc ON pt.Post_id == pc.Post_id
		LEFT JOIN Post_Likes AS pl ON pt.Post_id == pl.Post_id
		ORDER BY pt.Post_id;
	`

	// Execute the query against the connected database.
	rows, err := db.Query(query)
	if err != nil {
		log.Fatalf("Failed to execute query: %v", err)
	}
	// Ensure the result set is closed after we are done with it.
	defer rows.Close()

	// Process the query results
	var posts []Post

	for rows.Next() {
		var p Post
		if err := rows.Scan(&p.PostID, &p.PostType, &p.Comments, &p.Likes); err != nil {
			log.Printf("Failed to scan row: %v", err)
			continue
		}
		posts = append(posts, p)
	}

	// Check for errors that may have occurred during iteration
	if err := rows.Err(); err != nil {
		log.Fatalf("Error iterating over rows: %v", err)
	}

	fmt.Printf("Successfully queried and processed %d posts.\n", len(posts))

	// Marshal the Go struct slice into JSON
	jsonData, err := json.MarshalIndent(posts, "", "\t")
	if err != nil {
		log.Fatalf("Failed to marshal data to JSON: %v", err)
	}

	// Write the JSON data to a file
	err = ioutil.WriteFile(jsonOutputPath, jsonData, 0644)
	if err != nil {
		log.Fatalf("Failed to write JSON to file: %v", err)
	}

	fmt.Printf("Successfully saved combined post data to %s\n", jsonOutputPath)
}
