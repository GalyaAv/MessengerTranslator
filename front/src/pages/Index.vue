<template>
  <q-page class="flex flex-center">
    <q-card flat bordered class="full-width">
      <q-card-section>
        <q-chat-message
          v-for="(message, i) in messages"
          :key="i"
          :name="message.UserName"
          :text="[message.MessageText]"
          :sent="message.UserName == userName"

        />
      </q-card-section>
    </q-card>
    <!-- Панель действий -->
    <q-card class="full-width">
      <q-card-section>
        <q-input
          style="width: 40%; min-width: 200px"
          outlined
          dense
          v-model="userName"
          label="UserName"
        />
      </q-card-section>
      <q-card-section class="flex">
        <q-input
          class="mr-10"
          style="flex-grow: 1"
          outlined
          dense
          v-model="messageText"
          label="MessageText"
        />
        <q-btn
          depressed
          color="primary"
          @click="onSendClick"
          :disabled="!messageText.length"
        >
          Оправить
        </q-btn>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { computed, defineComponent } from "vue";
import { useStore } from 'vuex'
import API from "../api/api.js";

export default defineComponent({
  name: 'IndexPage',
  setup () {
    const $store = useStore()
    const userName = computed({
      get: () => $store.state.mes.userName,
      set: val => {
        $store.commit('mes/updateUserNameState', val)
      }
      })
    const messages = computed({
      get: () => $store.state.mes.messages,
      set: val => {
        $store.commit('mes/updateMessagesState', val)
      }
    })
    const intervalCtx = computed({
      get: () => $store.state.mes.intervalCtx,
      set: val => {
        $store.commit('mes/updateIntervalCtxState', val)
      }
    })
    const lastMsgID = computed({
      get: () => $store.state.mes.lastMsgID,
      set: val => {
        $store.commit('mes/updateLastMsgIDState', val)
      }
    })
    const messageText = computed({
      get: () => $store.state.mes.messageText,
      set: val => {
        $store.commit('mes/updateMessageTextState', val)
      }
    })
    return {
      $store, userName, messages, intervalCtx, lastMsgID,  messageText,
    }
  },
 async mounted() {
    // this.userName = "Login";
    this.intervalCtx = setInterval(async () => {
      try {
        const msg = await API.getMessage(this.lastMsgID);
        console.log(msg)
        if (typeof msg === typeof {}) {
          this.messages=msg
          console.log(msg)
          this.lastMsgID++
        }
      } catch (e) {}
    }, 1000);
  },
  unmounted() {
    clearInterval(this.intervalCtx);
  },
  methods: {
    // Реакция на кнопку отправки
    async onSendClick() {
      try {
        await API.sendMessage(this.userName, this.messageText);
        console.log("cleared");
        this.messageText = "";
      } catch (e) {
        console.error(e);
      }
    },
  },
})
</script>
<style scoped >
.flex-container {
    display: flex;
    border:1px solid #ccc;
    flex-direction: column  ;
    flex-wrap: wrap;
}
</style>
