<template>
  <div class="calculator-containter">
    <div class="title">Calculadora de Viagem</div>

    <div class="content">

      <div class="select-area">
        <h3>Calcule o Valor da Viagem</h3>
        <label class="city-dropdown">
          Destino
          <select>
            <option value="">Selecione o destino</option>
            <option v-for="city in cities" :key="city.cityName">{{ city.cityName }}</option>
          </select>
        </label>
        <label class="date-dropdown">
          Data
        </label>
        <button @click="buscarViagem">Buscar</button>
      </div>

      <div class="showdata-area">
        Nenhum dado selecionado
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'CalculatorSection',
  data() {
    return {
      cities: [],
    }
  },
  methods:{
    buscarViagem(){
      fetch('http://127.0.0.1:3000/transport')
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

<style scoped>
.calculator-container{
  padding: 20px;
  color: var(--dark);
  font-style: 'Roboto';
}

.title{
  background: var(--dark);
  color: var(--light);
  font-style: 'Roboto';
  font-size: 30px;

  padding: 1rem;
}

.content{
  display: flex;
  padding:1rem;
  gap:1rem;
}

.select-area{
  background: var(--grey);
  display: flex;
  flex-direction: column;
  padding: 2rem;
}

.city-dropdown select{
  width:200px;
  min-height: 35px;
  background: var(--light);
  border-radius: 3px;
  border:1px solid var(--dark);
  outline: none;
}
</style>