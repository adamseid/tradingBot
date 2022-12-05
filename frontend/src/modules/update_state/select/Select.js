
export const selectNavigatorState = (request, state, default_state) => {
    console.log('modules -> Select.selectNavigatorState(): STARTED')

    let filename = request.data
    let new_path = state.navigator.path + filename + '/'
    let tempPath = state.navigator.path
    let path_backward = state.navigator.path



    let filename_array = filename.split('.')
    let filename_extension = filename_array[filename_array.length-1]

    if (filename_extension === 'csv') {
        console.log('filename_extension === csv')
        state.navigator.current_file_type = 'csv'

        state.display.filename = filename
        state.display.path = new_path.slice(0, -1)

    } else {
        console.log('filename_extension !== csv')

        state.navigator.tempPath = tempPath
        state.navigator.path_backward = path_backward
        state.navigator.path = new_path
    
    }

    state.navigator.filename = filename

    console.log('modules -> Select.selectNavigatorState(): FINISHED')
    return state
}

