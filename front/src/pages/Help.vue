<template>
  <q-page class="flex flex-center ">
    <q-card bordered>
    <div class="login-panel">
    <q-card-section>
      <img
      alt="education"
      src="~assets/education.png"
      style="width: 150px; height: 150px"/>
    </q-card-section>
    <q-card-section>
        <q-card bordered>
          <q-card-section>
            <q-input dense flat v-model="trans" autofocus></q-input>
          </q-card-section>
          <q-card-section>
            {{retrans}}
          </q-card-section>
        </q-card>
    </q-card-section>
    </div>
    <div>
    <q-card-section>
        <q-btn class="full-width" @click="onSendClick(this.trans)">Перевод</q-btn>
    </q-card-section>
    </div>
    </q-card>
  </q-page>
</template>

<script>
import { defineComponent,ref } from 'vue';
import API from '../api/api'

export default defineComponent({
  name: 'HelpIndex',
  setup(){
    let trans=ref("");
    let retrans=ref("");
    return {
      trans, retrans
    }
  },
  methods: {
  // Реакция на кнопку отправки
    async onSendClick() {
      try {
        let tr = this.trans
        console.log(tr)
        this.retrans = await API.trans(tr);
      } catch (e) {
        console.error(e);
      }
    }
  },
})
</script>
<style lang="scss" scoped>
  .login-panel{
    display: flex;
    flex-direction: row;
  }
</style>
