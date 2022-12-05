import React, { Component } from 'react';
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
} from 'chart.js'

ChartJS.register(
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
)



const options = {};

const default_state = {
    graph_display: 'hide'
}

export default class Graph extends Component {
	constructor(props) {
		super(props);
		this.state = default_state;
	}

    
    showHide = (id) => {
        console.log('Graph.showHide(): STARTED')
        console.log(id)
        var graph = document.getElementById(id)

        if (graph.className === 'show'){
            graph.className = 'hide'
        } else {
            graph.className ='show'
        }

        

        console.log('Graph.showHide(): FINISHED')

    }



	render() {
		return (
			<div>
				<br />

				<div className="title">Graph</div>


                <div>
                    {this.props.graph.data.labels}
                </div>

                {this.props.state.display.graph.column_names.map((data, i) => (
                    <div  key={i} >
                        <button onClick={this.showHide.bind(this, i)}>{data}</button>
                        <div id={i} className={this.state.graph_display} style={{width: '800px', height: '450px', marginLeft: '50px'}}>
                            <Line data={{
                                labels: this.props.state.display.graph.last_few_rows[0],
                                datasets: [{
                                    data: this.props.state.display.graph.last_few_rows[i],
                                    backgroundColor: 'transparent',
                                    borderColor: '#f26c6d',				
                                    tension: 0,
                                    pointRadius: 0,
                                    pointHoverRadius: 0
                                }]
                            }} options={{
                                animation: false,
                                normalized: true,
                            }}></Line>
                        </div>
                    </div>
                ))}
			</div>
		);
	}
}
