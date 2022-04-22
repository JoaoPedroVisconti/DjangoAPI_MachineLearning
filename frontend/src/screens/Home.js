import React, { Component } from 'react'
import axios from 'axios'

import { Button, Container, Grid, TextField } from '@mui/material'

export default class Home extends Component {
  constructor() {
    super()
    this.state = {
      Dependents: '',
      ApplicantIncome: '',
      CoapplicantIncome: '',
      LoanAmount: '',
      Loan_Amount_Term: '',
      Credit_History: '',
      Gender: '',
      Married: '',
      Education: '',
      Self_Employed: '',
      Property_Area: '',
    }
  }

  componentDidMount() {
    const url = 'http://127.0.0.1:8000'

    axios
      .get(url + '/api/')
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err))
  }

  handleChange = (event) => {
    console.log(event.target.value)
    this.setState({
      [event.target.name]: event.target.value,
    })
  }

  handleSubmit = (event) => {
    event.preventDefault()

    const submission = {}
  }

  render() {
    return (
      <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
        <Grid item xs={6}>
          <form onSubmit={this.handleSubmit}>
            <TextField
              id='Dependents'
              name='Dependents'
              type='text'
              label='Dependents'
              onChange={this.handleChange}
            />
            <TextField
              id='ApplicantIncome'
              name='ApplicantIncome'
              type='text'
              label='ApplicantIncome'
              onChange={this.handleChange}
            />
            <TextField
              id='CoapplicantIncome'
              name='CoapplicantIncome'
              type='text'
              label='CoapplicantIncome'
              onChange={this.handleChange}
            />
            <TextField
              id='LoanAmount'
              name='LoanAmount'
              type='text'
              label='LoanAmount'
              onChange={this.handleChange}
            />
            <TextField
              id='Loan_Amount_Term'
              name='Loan_Amount_Term'
              type='text'
              label='Loan_Amount_Term'
              onChange={this.handleChange}
            />
            <TextField
              id='Credit_History'
              name='Credit_History'
              type='text'
              label='Credit_History'
              onChange={this.handleChange}
            />
            <TextField
              id='Gender'
              name='Gender'
              type='text'
              label='Gender'
              onChange={this.handleChange}
            />
            <TextField
              id='Married'
              name='Married'
              type='text'
              label='Married'
              onChange={this.handleChange}
            />
            <TextField
              id='Education'
              name='Education'
              type='text'
              label='Education'
              onChange={this.handleChange}
            />
            <TextField
              id='Self_Employed'
              name='Self_Employed'
              type='text'
              label='Self_Employed'
              onChange={this.handleChange}
            />
            <TextField
              id='Property_Area'
              name='Property_Area'
              type='text'
              label='Property_Area'
              onChange={this.handleChange}
            />
            <Button variant='contained' type='submit'>
              Submit
            </Button>
          </form>
        </Grid>
      </Grid>
    )
  }
}
