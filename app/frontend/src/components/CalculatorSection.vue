<template>
  <div class="calculator-container">
    <div class="title">Calculadora de Viagem</div>

    <div class="content">
      <div class="select-area">
        <h3>Calcule o Valor da Viagem</h3>
        <label class="city-dropdown">
          <h5>Destino </h5>
          <select v-model="selectedCity">
            <option value="">Selecione o destino</option>
            <option v-for="city in cities" :key="city.cityName" :value="city.cityName">{{ city.cityName }}</option>
          </select>
        </label>
        <!-- <div class="datepicker">
        </div> -->
        <button class="btn-search" @click="searchTrip">Buscar</button>
      </div>

      <div class="showdata-area">
        <div v-if="isLoading">Carregando...</div>
        <div v-else-if="bestTransport.fastest && bestTransport.cheapest">
          <h4>Essas são as melhores alternativas de viagem para a data selecionada.</h4>
          <br>
          <FlightOption :flight="bestTransport.fastest" :fastestOption="true"/>
          <FlightOption :flight="bestTransport.cheapest" />
        </div>
        <div v-else>
          Nenhum dado selecionado
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
      bestTransport: {},
      isLoading: false,
      showModal: false
    }
  },
  methods: {
    searchTrip() {
      if (!this.selectedCity) {
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
}

.title {
  background: var(--dark);
  color: var(--light);
  font-style: 'Roboto';
  font-size: 30px;
  padding: 1rem;
}

.content {
  display: flex;
  padding: 1rem;
  gap: 1rem;
}

.select-area {
  background: var(--grey);
  display: flex;
  flex-direction: column;
  padding: 2rem;
  gap: 10px;
}

.city-dropdown select {
  width: 200px;
  min-height: 35px;
  background: var(--light);
  border-radius: 3px;
  border: 1px solid var(--dark);
  outline: none;
}

.btn-search {
  background: var(--primary);
  color: var(--dark);
  outline: none;
}

.data-area-fast {
  background: var(--grey);
}
</style>
