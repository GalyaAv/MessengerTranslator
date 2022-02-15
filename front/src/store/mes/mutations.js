export const updateUserNameState = (state, val) => {
  state.userName = val
}
export const updateMessagesState = (state, val) => {
  state.messages.push(val) 
}
export const updateIntervalCtxState = (state, val) => {
  state.intervalCtx=val 
}
export const updateLastMsgIDState = (state, val) => {
  state.lastMsgID=val 
}
export const updateMessageTextState = (state, val) => {
  state.messageText=val 
}



export default function () {
  return {
      loginName: "",
      messages:[],
      intervalCtx:-null,
      lastMsgID: 0,
      messageText: "",

  }
}