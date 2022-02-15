<template>
  <q-page class="flex flex-center">
  <q-card  class="full-width">
    <q-card-section>  
      
      <b>Вы авторизированы как: </b> {{$store.state.mes.userName}} <br>
  </q-card-section>

  <q-card-section>
   <h3>Аннотация</h3>
   </q-card-section>
   </q-card>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import { useStore } from 'vuex'


export default defineComponent({
  name: 'AboutIndex',
  setup(){
     const $store = useStore()
    return{
      $store
    }
  }
})
</script>
