import React, { Component } from 'react';


export default class Debug extends Component {


    select = (filename) => {
		console.log(filename);
		this.props.filename(filename);
	};

	render() {
		return (
			<div>
                <div className='title'>Debug</div>

                <div className='title'>General</div>
                <div>websocket: {this.props.state.websocket}</div>


                <div>
                    <div className='title'>state.navigator</div>
                    <div>tempPath: {this.props.state.navigator.tempPath}</div>
                    <div>path_backward: {this.props.state.navigator.path_backward}</div>
                    <div>path: {this.props.state.navigator.path}</div>

                    <div>path_forward: {this.props.state.navigator.path_forward}</div>

                    <div>files: [     
                        {this.props.state.navigator.files.map((data, i) => (
                            <div key={i}>
                                <div>{data}, </div>
                            </div>
                        ))} ]
                    </div>
                    <div>current_file_type: {this.props.state.navigator.current_file_type}</div>
                    <div>filename: {this.props.state.navigator.filename}</div>
                </div>

                <div>
                    <div className='title'>state.graph</div>
                    <table>
                        <tr>
                            <th>1</th>
                            <th>2</th>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>4</td>
                        </tr>
                    </table>
                </div>
                <div>
                    <div className='title'>state.display.current</div>
                    <table>
                        <tr>
                            <th>filename</th>
                            <th>path</th>
                        </tr>
                        <tr>
                            <td>{this.props.state.display.filename}</td>
                            <td>{this.props.state.display.path}</td>
                        </tr>
                    </table>
                </div>
			</div>
		);
	}
}
