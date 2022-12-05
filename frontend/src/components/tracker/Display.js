import Graph from './display/Graph'
import Current from './display/Current'
import Info from './display/Info'


import React, { Component } from 'react';

class Display extends Component {


    connect = () => {
        console.log('Display.connect(): STARTED')

        
        let request = {
            location: ['Tracker', 'Display'],
            command: 'connect',
            data: ''
        }
		this.props.request(request);

        if (this.props.state.display.filename === 'none'){
            console.log('filename === none')
        } else {
            console.log('filename !== none')
            this.props.ws.send(
                JSON.stringify({
                    request: 'connect',
                    data: {
                        location: ['tracker', 'display'],
                        filename: this.props.state.display.filename,
                        path: this.props.state.display.path
                    }
                })
            );

        }


        console.log('Display.connect(): FINISHED')
    }

    render() {
        return (
            <div>
                <br/><br/>
                <div className='title'>Display</div>
               
                <br/><br/>
                <button onClick={this.connect}>Connect</button>
                <br/><br/><br/>
                
                <div>
                    <Info state={this.props.state}/>
                </div>

                
                <br/><br/><br/>

                <div>
                    <Current state={this.props.state}/>
                </div>
				<div>
					<Graph
						graph={this.props.state.graph}
                        state={this.props.state}
					/>
				</div>

            </div>
        );
    }
}

export default Display;