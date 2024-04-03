<template>
    <div>
      <h4 class="transport-title">{{ flight.name }}</h4>
      <p>Leito: {{ flight.bed }} (Completo)</p>
      <p>Tempo estimado: {{ flight.duration }}</p>
      <div>
        Preço: {{ price }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FlightOption',
    props: {
      flight: {
        type: Object,
        required: true
      },
      showPriceEcon: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      price() {
        return this.showPriceEcon ? this.flight.price_econ : this.flight.price_confort;
      }
    }
  }
  </script>
  
  <style scoped>
    .transport-title {
      background: var(--primary);
      padding: 10px;
      border-radius: 5px;
    }
  </style>