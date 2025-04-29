CREATE TABLE IF NOT EXISTS reports (
  id          SERIAL PRIMARY KEY,
  value       TEXT     NOT NULL,
  report_data JSONB    NOT NULL,
  pdf_content BYTEA    NOT NULL,
  created_at  TIMESTAMPTZ DEFAULT now()
);
