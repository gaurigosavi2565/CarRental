
document.addEventListener("DOMContentLoaded", () => {
    const carCards = document.querySelectorAll(".car-card")
  
    // Fade in animation for car cards
    carCards.forEach((card, index) => {
      card.style.opacity = "0"
      card.style.transform = "translateY(20px)"
      card.style.transition = "opacity 0.5s ease, transform 0.5s ease"
  
      setTimeout(() => {
        card.style.opacity = "1"
        card.style.transform = "translateY(0)"
      }, 100 * index)
    })
  
    // Hover effect for car cards
    carCards.forEach((card) => {
      card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.05)"
        card.style.boxShadow = "0 8px 12px rgba(0, 0, 0, 0.2)"
      })
  
      card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)"
        card.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)"
      })
    })
  
    // Smooth scroll to top when clicking on logo
    const logo = document.querySelector(".logo")
    logo.addEventListener("click", (e) => {
      e.preventDefault()
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      })
    })
  })
  
  