<template>
    <aside class="side-bar">
        <img class="company-logo" alt="Vue logo" src="../assets/logo.png">
        <a><img src="../assets/calculator_icon.png" width="20px">
          <label><i class="fa fa-calculator" aria-hidden="true"></i> Calculdora de Viagem </label>
        </a>
    </aside>
</template>
  
  <script>
  export default {
    name: 'SideBar'
  }
  
  </script>
  
  <style scoped>
  aside{
    display: flex;
    flex-direction: column;

    background-color: var(--dark);
    color: var(--light);

    width: var(--sidebar-width);
    overflow: hidden;
    min-height: 100vh;
    padding: 1rem;
    
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 24px;
  }

  .company-logo{
    margin-bottom:1rem;
    width: 250px;
  }
  </style>
  