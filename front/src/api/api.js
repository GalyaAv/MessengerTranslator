import Axios from 'axios'

const axios = Axios.create({
    baseURL: 'http://localhost:5000',
})

export default class API {
    // Получает сообщение по id
    static async getMessage(id) {
        const resp = await axios.get(`/mes/${id}`)
        return resp.data
    }

    // Отправка сообщения
    static async sendMessage(UserName, MessageText) {

            var currenttime = new Date()
            await axios.post(`/mes`, {
                MessageText, // text: text
                UserName,
                TimeStamp: currenttime.toLocaleTimeString()
            })
        }
        // Отправка сообщения
    static async trans(text) {
        const resp = await axios.post(`/trans`, {
            text: text
        })
        return resp.data
    }
}