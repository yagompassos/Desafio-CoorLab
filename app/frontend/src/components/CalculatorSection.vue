<template>
  <div class="calculator-container">
    <div class="title">
      <img src="../assets/calculator_icon.png" width="20px">
      Calculadora de Viagem
    </div>

    <div class="content">
      <div class="select-area">
        <h4>Calcule o Valor da Viagem</h4> <br>
        <label class="city-dropdown">
          <h5>Destino </h5><br>
          <select class="input-box" v-model="selectedCity">
            <option value="">Selecione o destino</option>
            <option v-for="city in cities" :key="city.cityName" :value="city.cityName">{{ city.cityName }}</option>
          </select>
        </label>
        <h5>Data </h5>
          <input class="input-box" type="date" placeholder="Selecione uma data" v-model="selectedDate" /><br>
        <button class="btn-search" @click="searchTrip">Buscar</button>
      </div>

      <div class="showdata-area">
        <div v-if="isLoading">Carregando...</div>
        <div v-else-if="bestTransport.fastest && bestTransport.cheapest">
          <h4>Estas são as melhores alternativas de viagem para a data selecionada.</h4>
          <br>
          <FlightOption :flight="bestTransport.fastest" :fastestOption="true"/>
          <FlightOption :flight="bestTransport.cheapest" />
        </div>
        <div v-else>
          <h4 class="no-data-msg">Nenhum dado selecionado.</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FlightOption from './FlightOption.vue';

export default {
  name: 'CalculatorSection',
  components: {
    FlightOption
  },
  data() {
    return {
      cities: [],
      selectedCity: '',
      selectedDate: '',
      bestTransport: {},
      isLoading: false,
      showModal: false
    }
  },
  methods: {
    searchTrip() {
      if (!this.selectedCity || !this.selectedDate) {
        alert("Insira os valores para realizar a cotação");
        return
      }
      this.isLoading = true
      fetch(`http://127.0.0.1:3000/best_transport/${this.selectedCity}`)
        .then(response => response.json())
        .then(data => {
          this.bestTransport = data
          this.isLoading = false
        })
        .catch(error => {
          console.error('Erro ao buscar transporte:', error)
          this.isLoading = false
        })
    }
  },
  mounted() {
    fetch('http://127.0.0.1:3000/cities')
      .then((res) => res.json())
      .then(data => this.cities = data)
      .catch(err => console.log(err.message))
  },
}
</script>

<style scoped>
.calculator-container {
  color: var(--dark);
  font-style: 'Roboto';
  box-shadow: 3px 3px 1em #777;
  margin-top: 150px;
  margin-left: 50px;
  border-radius: 10px;
  width: 1100px;
  padding: 0; 
}

.title {
  background: var(--dark);
  color: var(--light);
  font-style: 'Roboto';
  font-size: 30px;
  padding: 1rem;
  border-radius: 10px 10px 0 0;
}

.content {
  display: flex;
  padding: 1rem;
  gap: 1rem;
  height: 500px;
}

.select-area {
  background: var(--grey);
  display: flex;
  flex-direction: column;
  padding: 2rem;
  gap: 10px;
  justify-content: center;
  width: 550px;
}

.input-box{
  width: 100%;
  min-height: 35px;
  background: var(--light);
  color: #777;
  border-radius: 3px;
  border: 1px solid rgba(126, 126, 126, 0.329);
  outline: none;
  font-size: 14px;
  padding: 10px;
}

option{
  color: #777;
  height: 10px;
}
h5{
  margin-top: 5px;
}
.btn-search {
  background: var(--primary);
  color: var(--dark);
  font-weight: bold;
  border-radius: 5px;
  border: none;
  width: 60%;
  height: 30px;
  align-self: center;
}

.no-data-msg{
  font-size: large;
}

.showdata-area { 
  margin: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
