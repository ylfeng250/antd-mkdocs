## zh-CN

在实现全选效果时，你可能会用到 `indeterminate` 属性。

## en-US

The `indeterminate` property can help you to achieve a 'check all' effect.
```tsx
import React, { useState } from 'react';
import { Checkbox, Divider } from 'antd';
import type { CheckboxProps, GetProp } from 'antd';

type CheckboxValueType = GetProp<typeof Checkbox.Group, 'value'>[number];

const CheckboxGroup = Checkbox.Group;

const plainOptions = ['Apple', 'Pear', 'Orange'];
const defaultCheckedList = ['Apple', 'Orange'];

const App: React.FC = () => {
  const [checkedList, setCheckedList] = useState<CheckboxValueType[]>(defaultCheckedList);

  const checkAll = plainOptions.length === checkedList.length;
  const indeterminate = checkedList.length > 0 && checkedList.length < plainOptions.length;

  const onChange = (list: CheckboxValueType[]) => {
    setCheckedList(list);
  };

  const onCheckAllChange: CheckboxProps['onChange'] = (e) => {
    setCheckedList(e.target.checked ? plainOptions : []);
  };

  return (
    <>
      <Checkbox indeterminate={indeterminate} onChange={onCheckAllChange} checked={checkAll}>
        Check all
      </Checkbox>
      <Divider />
      <CheckboxGroup options={plainOptions} value={checkedList} onChange={onChange} />
    </>
  );
};

export default App;
```
