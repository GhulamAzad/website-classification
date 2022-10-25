const humburgerMenuIcon = {
    open: ` <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
      xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd"
          d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
          clip-rule="evenodd"></path>
  </svg>`,
    close: `  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
      stroke="currentColor" class="w-6 h-6">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
  </svg>`,
  };
  
  const humburgerMenuContainer = document.getElementById("humburger-icon");
  const mobileNav = document.getElementById("navbar-default");
  
  let isNavOpen = false;
  
  const humburgerMenuIconHandler = () => {
    if (isNavOpen) {
      humburgerMenuContainer.innerHTML = humburgerMenuIcon.close;
    } else {
      humburgerMenuContainer.innerHTML = humburgerMenuIcon.open;
    }
    isNavOpen = !isNavOpen;
  };
  
  function navToggle() {
    humburgerMenuIconHandler();
  
    mobileNav.classList.toggle("block");
    mobileNav.classList.toggle("hidden");
  }
  
  //Team
  const teams = document.querySelectorAll(".team-card");
  const teamImages = document.querySelectorAll(".team-card-image");
  
  teamImages.forEach((team) => {
    team.addEventListener("mouseenter", () => {
      teams.forEach((team) => {
        team.classList.add("team-card-hover-out");
      });
      team.parentElement.classList.remove("team-card-hover-out");
      team.parentElement.classList.add("team-card-hover");
    });
  
    team.addEventListener("mouseleave", () => {
      teams.forEach((team) => {
        team.classList.remove("team-card-hover");
        team.classList.remove("team-card-hover-out");
      });
    });
  });
  
  //init
  // humburgerMenuIconHandler();
  
  // document.addEventListener("click", () => {
  //   const player = document.querySelector("#player");
  //   player.play();
  // });
  