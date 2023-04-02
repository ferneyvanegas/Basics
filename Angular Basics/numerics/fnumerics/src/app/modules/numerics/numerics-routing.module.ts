import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// Component
import { TableComponent } from './table/table.component';

const routes: Routes = [
  {
    path: '',
    component: TableComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NumericsRoutingModule { }
