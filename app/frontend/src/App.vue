<template>
  <div class="app-container">
    <SideBar />
    <div class="page-content">
      <HeaderSection class="header-container" />
      <CalculatorSection class="calc-container"/>
    </div>
  </div>
</template>

<script>
import CalculatorSection from './components/CalculatorSection.vue'
import SideBar from './components/SideBar.vue'
import HeaderSection from './components/HeaderSection.vue'

export default {
  name: 'App',
  components: {
    CalculatorSection,
    SideBar,
    HeaderSection
  }
}
</script>

<style>
:root {
  --primary: #03a8b5;
  --light: #ecf6ff;
  --dark: #2b2f40;
  --grey: #e7e7e77e;
  --sidebar-width: 300px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}

body{
  background: var(--light);
}

.app-container{
  display: flex; 

}

.page-content{
  display: flex; 
  flex-direction: column;
}
.header-containter{
  width: 100%;
}
.calc-container{
  margin-top: 150px  ;
  padding:2rem;
}

</style>
