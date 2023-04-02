import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { NumericsRoutingModule } from './numerics-routing.module';
import { TableComponent } from './table/table.component';


@NgModule({
  declarations: [
    TableComponent
  ],
  imports: [
    CommonModule,
    NumericsRoutingModule,
    FormsModule
  ]
})
export class NumericsModule { }
