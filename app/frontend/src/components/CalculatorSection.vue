<template>
  <div class="calculator-container">
    <div class="title">Calculadora de Viagem</div>

    <div class="content">

      <div class="select-area">
        <h3>Calcule o Valor da Viagem</h3>
        <label class="city-dropdown">
          Destino
          <select v-model="selectedCity">
            <option value="">Selecione o destino</option>
            <option v-for="city in cities" :key="city.cityName" :value="city.cityName">{{ city.cityName }}</option>
          </select>
        </label>
        <button @click="searchTrip">Buscar</button>
      </div>

      <div class="showdata-area">
        <div v-if="isLoading">Carregando...</div>
        <div v-else-if="bestTransport.fastest && bestTransport.cheapest">
          <h4>Opção mais rápida:</h4>
          <p>Nome: {{ bestTransport.fastest.name }}</p>
          <p>Duração: {{ bestTransport.fastest.duration }}</p>
          <p>Preço: {{ bestTransport.fastest.price_econ }}</p>

          <h4>Opção mais econômica:</h4>
          <p>Nome: {{ bestTransport.cheapest.name }}</p>
          <p>Duração: {{ bestTransport.cheapest.duration }}</p>
          <p>Preço: {{ bestTransport.cheapest.price_econ }}</p>
        </div>
        <div v-else-if="bestTransport.option">
          <h4>Melhor Opção</h4>
          <p>Nome: {{ bestTransport.option.name }}</p>
          <p>Duração: {{ bestTransport.option.duration }}</p>
          <p>Preço: {{ bestTransport.option.price_econ }}</p>
        </div>
        <div v-else>
          Nenhum dado selecionado
        </div>
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
      selectedCity: '',
      bestTransport: {},
      isLoading: false
    }
  },
  methods:{
    searchTrip() {
      if (!this.selectedCity) {
        alert('Por favor, selecione uma cidade.')
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
  mounted(){
    fetch('http://127.0.0.1:3000/cities')
      .then ((res) => res.json())
      .then (data => this.cities = data)
      .catch(err => console.log(err.message))
  }
}
</script>

<style scoped>
.calculator-container {
  padding: 20px;
  color: var(--dark);
  font-style: 'Roboto';
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
}

.city-dropdown select {
  width: 200px;
  min-height: 35px;
  background: var(--light);
  border-radius: 3px;
  border: 1px solid var(--dark);
  outline: none;
}
</style>
