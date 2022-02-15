export default function () {
  return {
    // messages: [
    //   {
    //     UserName: "RusAl",
    //     MessageText: "Добрый день",
    //     TimeStamp: "12:40",
    //   },
    //   {
    //     UserName: "Ёжик",
    //     MessageText: "Привет",
    //     TimeStamp: "12:43",
    //   },
    //   {
    //     UserName: "RusAl",
    //     MessageText: "Как дела?",
    //     TimeStamp: "12:44",
    //   },
    // ],
    messages: [],
    userName:"Ёжик",
    intervalCtx: null,
    lastMsgID: 0,
    messageText: "",
  }
}
