resource "aws_db_instance" "postgres" {

  engine         = "postgres"
  engine_version = "15"

  instance_class = "db.t3.micro"

  allocated_storage = 20

  db_name  = "logs"
  username = "admin"
  password = "password"

  skip_final_snapshot = true
}