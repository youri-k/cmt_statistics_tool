CREATE TABLE revision_metareview (
	overall_rating TEXT NOT NULL, 
	comments TEXT NOT NULL, 
	revision_id INTEGER NOT NULL, 
	reviewer_id INTEGER NOT NULL, 
	PRIMARY KEY (revision_id, reviewer_id), 
	FOREIGN KEY(revision_id) REFERENCES revision (id), 
	FOREIGN KEY(reviewer_id) REFERENCES people (id)
)
