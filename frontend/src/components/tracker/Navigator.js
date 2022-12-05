import React, { Component } from 'react';


export default class Navigator extends Component {

    listDir = () => {
        console.log('Navigator.listDir(): STARTED');
        this.props.ws.send(
            JSON.stringify({
                request: 'listdir',
                data: {
                    location: ['navigator'],
                    path: this.props.navigator.path
                }
            })
        );
        console.log('Navigator.listDir(): FINISHED');
    };

    requestCSVData = () => {
        console.log('Navigator.requestCSVData(): STARTED')
        console.log('Navigator.requestCSVData(): FINISHED')

    }


    select = (filename) => {
        console.log('Navigator.select(): STARTED')
		console.log(filename);

        let request = {
            location: ['Tracker', 'Navigator'],
            command: 'select',
            data: filename
        }
		this.props.request(request);

        if (this.props.navigator.current_file_type === 'directory'){
            console.log('current_file_type === directory')
            this.listDir()

        } else if(this.props.navigator.current_file_type === 'csv'){
            console.log('current_file_type === csv')
            this.requestCSVData()
        }

        console.log('Navigator.select(): FINISHED')
	};

    goBack = (location) => {
        console.log('Navigator.goBack(): STARTED');
        console.log(location);
        this.props.location(location);
        this.listDir()
        console.log('Navigator.goBack(): FINISHED');
    }

	render() {
		return (
			<div>
				<br />

				<div className="title">Navigator</div>
                <button onClick={this.listDir}>listDir</button>
                <button onClick={this.goBack.bind(this, ['Tracker', 'Navigator'])}>Go Back</button>
                <br/><br/><br/>
                {this.props.navigator.files.map((data, i) => (
                    <div key={i}>
                        <button onClick={this.select.bind(this,data)}>{data}</button>
                    </div>
                ))}
			</div>
		);
	}
}
