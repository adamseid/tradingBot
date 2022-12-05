import React, { Component, useImperativeHandle } from 'react';
import Navigator from './tracker/Navigator'
import Debug from './tracker/Debug'
import Display from './tracker/Display'
import {funcName, test, goBack, updateState} from '../modules/Tracker'

const default_state = {
	component: {
		navigator: 'hide',
		debug: 'show'
	},
	button: {
		go_back: 'hide',
		navigator: 'show'
	},

	navigator: {
		test: 'hi',
		path_backward: '',
		path: '../storage/',
		path_forward: '',
		tempPath: '../storage/',
		files: [],
		current_file_type: 'directory',
		filename: 'none'
	},

	graph: {

		test: 1,
		data: {
			labels: [1, 2, 3],
			datasets: [{
				data: [4, 5, 7],
				backgroundColor: 'transparent',
				borderColor: '#f26c6d',
				tension: 0.4,
				pointRadius: 0,
				hoverPointRadius: 0
			}]
		},
		options: {
			elements: {
				point: {
					radius: 0
				}
			}
		}
	},

	websocket: 'disconnected',

	unit: 'kg',

	display: {
		filename: 'none',
		path: 'none',
		current: {
			time: 'none',
			price: 'none',
			change_price: 'none',
			rsi: 'none',
			coin_allocation: 'none',
			cash_allocation: 'none',
			coin_balance: 'none',
			cash_balance: 'none',
			total_balance: 'none',
			profit: 'none',
			total_profit: 'none'
		},
		current_array: [],
		current_column_names: [],
		graph: {
			column_names: [],
			last_few_rows: [],
		}
	},


}

export default class Tracker extends Component {
	ws = new WebSocket('ws://localhost:8000/ws/websocket/' + 'tracker' + '/');

	componentDidMount() {
		this.ws.onopen = () => {
			console.log('connected');
			this.setState({websocket: 'connected'})
		}
		this.ws.onmessage = (e) => {
			console.log(e);


			let data = JSON.parse(e.data).data;
			let command = JSON.parse(e.data).command

			//console.log(data.location[0])

			if (data.location[0] === 'navigator'){
				console.log('onmessage() location layer 0: navigator');
				this.setState((prevState) => {
					let navigator = Object.assign({}, prevState.navigator);
					navigator.files = data.listdir;
					return { navigator };
				});

			};

			console.log(command)

			if (command === 'update-current') {
				console.log('command === update-current')
				let request = {
					command: 'update-current',
					data: data
				};
				let state = updateState(request, this.state, default_state);
				this.setState((prevState) => {
					let display = Object.assign({}, prevState.display)
					display = state.display
					return { display }
				})
			}

			if (command === 'update-graph') {
				console.log('command === update-graph')
				let request = {
					command: 'update-graph',
					data: data
				}
				let state = updateState(request, this.state, default_state)
			}






		}
		this.ws.onclose = () => {
			console.log('disconnected')
			this.setState({websocket: 'disconnected'})
		}
	}

	componentDidUpdate(prevProps, prevState, snapshot){
		console.log('Tracker.componentDidUpdate(): STARTED')

		if (prevState.navigator.path !== this.state.navigator.path) {
			console.log('NOT EQUAL')

			let new_path = this.state.navigator.path

			this.setState((prevState) => {
				let navigator = Object.assign({}, prevState.navigator);
				navigator.tempPath = new_path
				return { navigator }
			});
			this.navigator.current.listDir();
		}

		//this.navigator.current.listDir();
		console.log('Tracker.componentDidUpdate(): FINISHED')

	}

	constructor(props) {
		super(props);
		this.state = default_state;
		this.navigator = React.createRef()

	}



	goBack = (location) => {
		console.log('Tracker.goBack(): STARTED')
		let request = {
			location: location,
			command: 'go-back'
		};
		let state = updateState(request, this.state, default_state);
		this.setState((prevState) => {
			let navigator = Object.assign({}, prevState.navigator)
			let button = Object.assign({}, prevState.button)
			let component = Object.assign({}, prevState.component)
			navigator = state.navigator
			button = state.button
			component = state.component
			return {navigator, component, button}
		})
		console.log('Tracker.goBack(): FINISHED')
	}

	showNavigator = () => {
		console.log('Tracker.showNavigator(): STARTED')
		this.setState((prevState) => {
			let button = Object.assign({}, prevState.button);
			let component = Object.assign({}, prevState.button);
			button.go_back = 'show';
			button.navigator = 'hide';
			component.navigator = 'show';
			return { button, component }
		});
		console.log('Tracker.showNavigator(): FINISHED')
	}


	select = (request) => {
		console.log('Tracker.select(): STARTED')


		let state = updateState(request, this.state, default_state);
		console.log(state)

		/*
		let filename = request.data

		let new_path = this.state.navigator.path + filename + '/'
		this.setState((prevState) => {
			let navigator = Object.assign({}, prevState.navigator);
			navigator.tempPath = navigator.path
			navigator.path_backward = navigator.path
			navigator.path = new_path
			return { navigator }
		})
		*/

		this.setState((prevState) => {
			let navigator = Object.assign({}, prevState.navigator)
			let display = Object.assign({}, prevState.display)
			navigator = state.navigator
			display = state.display
			return { navigator, display }
		})
		console.log('Tracker.select(): FINISHED')
	};

	connect = (request) => {
		console.log('Tracker.connect(): STARTED')

		console.log(request)
		let state = updateState(request, this.state, default_state);
		console.log(state)

		console.log('Tracker.connect(): FINISHED')

	}


	render() {
		return (
			<div>
				<br />
				<div className="title">Tracker</div>




				<br/><br/><br/>
				<div className={this.state.component.debug}>
					<Debug
						state={this.state}
					/>
				</div>

				<br/><br/><br/>
				<button
					className={this.state.button.go_back}
					onClick={this.goBack.bind(this, ['Tracker'])}
				>
					Go Back
				</button>
				<button
					className={this.state.button.navigator}
					onClick={this.showNavigator}
				>
					Launch Navigator
				</button>
							
		
				<div className={this.state.component.navigator}>
					<Navigator
						ws={this.ws}
						navigator={this.state.navigator}
						request={this.select}
						location={this.goBack}
						ref={this.navigator}
					/>
				</div>



				<div>
					<Display
						ws={this.ws}
						state={this.state}
						request={this.connect}
					/>
				</div>

			</div>
		);
	}
}
