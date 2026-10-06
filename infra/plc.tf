# Configuración de infraestructura - PLC Maipo Sur
# ⚠️ DEFECTO SEMBRADO: acceso abierto a internet

resource "aws_security_group" "plc" {
  name        = "plc-maipo-sur"
  description = "Acceso al PLC de dosificación de cloro"

  ingress {
    description = "Modbus desde cualquier origen (INSEGURO)"
    from_port   = 502
    to_port     = 502
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]   # ⚠️ Abierto a todo internet
  }

  ingress {
    description = "HTTP del panel HMI"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]   # ⚠️ Abierto a todo internet
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "plc" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  # ⚠️ DEFECTO: credencial de fábrica
  user_data = <<-EOF
    #!/bin/bash
    echo "admin:admin123" | chpasswd
    systemctl start modbus-server
  EOF

  tags = {
    Name = "PLC-Maipo-Sur"
  }
}
