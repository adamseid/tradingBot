import React, { Component } from 'react';

class Current extends Component {
    render() {
        return (
            <div>
                <div className='title'>Current</div>
                <table>
                    <tr>
                        {this.props.state.display.current_column_names.map((data, i) => (
                            <th key={i}>
                                <div>{data}</div>
                            </th>
                        ))}
                    </tr>
                    <tr>
                        {this.props.state.display.current_array.map((data, i) => (
                            <td key={i}>
                                <div>{data}</div>
                            </td>
                        ))}
                    </tr>
                </table>
            </div>
        );
    }
}

export default Current;