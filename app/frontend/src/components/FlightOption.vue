<template>
    <div class="flight-option">
      <div class="icon">
        <img :src="iconPath" alt="Ícone do tipo de voo">
      </div>
      <div class="data">
        <h4 >{{ flight.name }}</h4>
        <p>{{ showSeatType }}: {{ seatValue }} ({{ showSeatStatus }})</p>
        <p>Tempo estimado: {{ flight.duration }}</p>
      </div>
      <div class="price">
        <h4>Preço:</h4> 
        <p>{{ price }}</p>
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
      },
      fastestOption: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      price() {
        return this.fastestOption ? this.flight.price_confort : this.flight.price_econ;
      },
      iconPath() {
        return this.fastestOption ? require('../assets/time_icon.png') : require('../assets/econ_icon.png');
      },
      showSeatType() {
        return this.fastestOption ? 'Leito' : 'Poltrona';
      },
      showSeatStatus() {
        return this.fastestOption ? 'Completo' : 'Convencional';
      },
      seatValue(){
        return this.fastestOption ? this.flight.bed : this.flight.seat;
      }
    }
  };
  </script>
  
  <style scoped>
  .flight-option {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .icon {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 70px;
    height: 100px;
    background: var(--primary);
    border-radius: 10px 0 0 10px;
  }
  
  img {
    width: 50px;
  }
  
  .data {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 100px;
    width: 300px;
    background: var(--grey);
    padding: 10px;
    gap:3px;
    border-radius: 0 10px 10px 0 ;
  }

  .price{
    margin-left: 15px;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    height: 100px;
    width: 200px;
    background: var(--grey);
    border-radius: 10px;
    padding: 20px;
    gap:3px;
  }
  </style>
  