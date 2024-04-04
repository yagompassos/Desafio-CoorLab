<template>
  <div class="popup">
    <div class="popup-inner">
      <img src="../assets/alert_icon.png" width="100px">
      <h2>Insira os valores para iniciar a cotação.</h2>
      <button class="btn-close" @click="closeModal">Fechar</button>
    </div>
  </div>
  </template>
  
  <script>
  export default {
    name: 'ModalAlert',
    methods: {
      closeModal() {
        this.$emit('close-modal')
      }
    }
  }
  </script>
  <style scoped>
  .popup{
    position: absolute;
    top:0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    border: solid 1px;
    background-color: rgba(0, 0, 0 , 0.2);
    
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .popup-inner{
    background: var(--light);
    color:#666;
    padding: 32px;
    width: 500px;
    height: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap:30px;
    text-align: center;
  }

  .btn-close {
    background: var(--primary);
    color: var(--dark);
    font-weight: bold;
    border-radius: 5px;
    border: none;
    width: 210px;
    height: 30px;
    cursor: pointer;
  }

  </style>