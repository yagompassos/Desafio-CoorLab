<template>
  <div>
    <select>
      <option v-for="city in cities" :key="city.cityName">{{ city.cityName }}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'CalculatorSection',
  data() {
    return {
      cities: []
    }
  },
  mounted(){
    fetch('http://127.0.0.1:3000/cities')
    .then ((res) => res.json())
    .then (data => this.cities = data)
    .catch(err => console.log(err.message))
  }
}
</script>

<style>
</style>
