import {goBack, select, connect, updateCurrent, updateGraph} from './update_state/UpdateState'

export  const funcName = () => {
    console.log('funcName()')
}
  
export const test = () => {
    console.log('modules -> Tracker.test(): STARTED')
    console.log('modules -> Tracker.test(): FINISHED')
}

export const updateState = (request, state, default_state) => {
    console.log('modules -> Tracker.updateState(): STARTED')

    console.log(request)
    console.log(state)
    console.log(default_state)

    if (request.command === 'go-back') {
        console.log('command === go-back')
        state = goBack(request.location, state, default_state)
    }

    if (request.command === 'select') {
        console.log('command === select')
        state = select(request, state, default_state)
    }

    if (request.command === 'connect') {
        console.log('command === connect')
        state = connect(request, state, default_state)
    }

    if (request.command === 'update-current') {
        console.log('command === update-current')
        state = updateCurrent(request, state, default_state)
    }

    if (request.command === 'update-graph') {
        console.log('command === update-graph')
        state = updateGraph(request, state, default_state)
    }

    console.log('modules -> Tracker.updateState(): FINISHED')

    return state;
}