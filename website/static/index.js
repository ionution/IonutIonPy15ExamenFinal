function deleteService(serviceId) {
  fetch("/delete-service", {
    method: "POST",
    body: JSON.stringify({ serviceId: serviceId }),
  }).then((_res) => {
    window.location.href = "/postService";
  });
}