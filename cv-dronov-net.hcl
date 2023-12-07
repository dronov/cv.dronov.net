job "cv-dronov-net" {
  type = "service"

  group "cv-dronov-net" {
    count = 1
    network {
      port "web" {
        static = 3000
      }
    }
    service {
      name     = "cv-dronov-net-svc"
      provider = "nomad"
    }

    restart {
      attempts = 2
      interval = "5m"
      delay = "15s"
      mode = "fail"
    }

    task "cv-dronov-net-task" {
      driver = "docker"
      config {
        image = "localhost:5000/cv-dronov-net:latest"
        ports = ["web"]
      }
    }
  }
}
