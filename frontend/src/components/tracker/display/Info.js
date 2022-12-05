import React, { Component } from 'react';

class Info extends Component {
    render() {
        return (
            <div>
                <div className='title'>Info</div>
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
        );
    }
}

export default Info;