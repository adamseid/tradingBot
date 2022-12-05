
export const updateNavigatorState = (state, default_state) => {
    console.log('GoBack.updateNavigatorState(): STARTED')
    console.log(state)
    console.log(default_state)

    //state.navigator.path = 'sdlfjslejf'

    let path = state.navigator.path_backward
    let path_forward = state.navigator.path
    //console.log(path.substring(0, path.lastIndexOf('/')))
    console.log(path)

    let path_backward = path.substring(0, path.lastIndexOf('/'))
    path_backward = path_backward.substring(0, path_backward.lastIndexOf('/')) + '/'

    console.log(path_backward)

    state.navigator.path = path
    state.navigator.path_forward = path_forward
    state.navigator.path_backward = path_backward

    console.log(path)

    state.navigator.current_file_type = 'directory'

    let path_array = path.split('/')
    state.navigator.filename = path_array[path_array.length-2]

    console.log('GoBack.updateNavigatorState(): FINISHED')
    return state
}



export const updateTrackerState = (state, default_state) => {
    console.log('GoBack.updateTrackerState(): STARTED')
    console.log(state)
    console.log(default_state)

    state.button = default_state.button
    state.component = default_state.component
    console.log(state.navigator)
    console.log(default_state.navigator)
    state.navigator = default_state.navigator
    console.log(state.navigator)


    console.log('GoBack.updateTrackerState(): FINISHED')
    return state
}

