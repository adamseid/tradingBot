import React, { Component } from 'react';


export default class Navigator extends Component {

    listDir = () => {
        console.log('Navigator.listDir(): STARTED')
        this.props.ws.send(
            JSON.stringify({
                request: 'listdir',
                data: {
                    location: {
                        Tracker: 'navigator'
                    },
                    path: this.props.navigator.path
                }
            })
        )
        console.log('Navigator.listDir(): FINISHED')
    }



	render() {
		return (
			<div>
				<br />
				<div className="title">Navigator</div>
                <button onClick={this.listDir}>listDir</button>
                {this.props.navigator.files.map((data, i) => (
                    <div key={i}>
                        <button>{data}</button>
                    </div>
                ))}
			</div>
		);
	}
}
