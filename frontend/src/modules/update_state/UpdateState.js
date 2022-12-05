
import {updateNavigatorState, updateTrackerState} from './go_back/GoBack'
import { selectNavigatorState } from './select/Select'
import { connectDisplayState } from './connect/Connect'


export const goBack = (location, state, default_state) => {
    console.log('modules -> UpdateState.goBack(): STARTED')

    if (location[1] === 'Navigator'){
        console.log('Navigator')
        state = updateNavigatorState(state, default_state)
    }else if (location[0] == 'Tracker'){
        console.log('Tracker')
        state = updateTrackerState(state, default_state)
    }

    console.log('modules -> UpdateState.goBack(): FINISHED')
    return state
}


export const select = (request, state, default_state) => {
    console.log('modules -> UpdateState.select(): STARTED')

    if (request.location[1] === 'Navigator') {
        console.log('request.location[1] === Navigator')
        state = selectNavigatorState(request, state, default_state)
    }

    console.log('modules -> UpdateState.select(): FINISHED')
    return state
}

export const connect = (request, state, default_state) => {
    console.log('modules -> UpdateState.connect(): STARTED')

    if (request.location[1] === 'Display') {
        console.log('request.location[i] === Display')
        state = connectDisplayState(request, state, default_state)
    }

    console.log('modules -> UpdateState.connect(): FINISHED')
    return state
}


export const updateCurrent = (request, state, default_state) => {
    console.log('modules -> UpdateState.updateCurrent(): STARTED')
    console.log(request)
    state.display.current.time = request.data.last_row[0]
    state.display.current.price = request.data.last_row[1]
    state.display.current.change_price = request.data.last_row[2]
    state.display.current.rsi = request.data.last_row[3]
    state.display.current.coin_allocation = request.data.last_row[4]
    state.display.current.cash_allocation = request.data.last_row[5]
    state.display.current.coin_balance = request.data.last_row[6]
    state.display.current.cash_balance = request.data.last_row[7]
    state.display.current.total_balance = request.data.last_row[8]
    state.display.current.profit = request.data.last_row[9]
    state.display.current.total_profit = request.data.last_row[10]
    state.display.current_array = request.data.last_row
    state.display.current_column_names = request.data.column_names
    console.log('modules -> UpdateState.updateCurrent(): FINISHED')
    return state
}

export const updateGraph = (request, state, default_state) => {
    console.log('modules -> UpdateState.updateGraph(): STARTED')

    state.display.graph.column_names = request.data.column_names
    state.display.graph.last_few_rows = request.data.last_few_rows


    console.log('modules -> UpdateState.updateGraph(): FINISHED')

    return state
}