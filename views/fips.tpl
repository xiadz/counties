%include header

<h2>States</h2>
<table>
    <tr> <th>State</th> <th>Abbr</th> <th>FIPS</th> </tr>
    %for state in states:
    <tr> <td>{{state.name}}</td> <td>{{state.abbr}}</td> <td>{{state.fips}}</td> </tr>
    %end
</table>
