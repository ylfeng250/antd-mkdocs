## zh-CN

你可以通过设置 `maxCount` 约束最多可选中的数量，当超出限制时会变成禁止选中状态。

## en-US

You can set the `maxCount` prop to control the max number of items can be selected. When the limit is exceeded, the options will become disabled.
```tsx
import React from 'react';
import { DownOutlined } from '@ant-design/icons';
import { Select } from 'antd';

const MAX_COUNT = 3;

const App: React.FC = () => {
  const [value, setValue] = React.useState<string[]>(['Ava Swift']);

  const suffix = (
    <>
      <span>
        {value.length} / {MAX_COUNT}
      </span>
      <DownOutlined />
    </>
  );

  return (
    <Select
      mode="multiple"
      maxCount={MAX_COUNT}
      value={value}
      style={{ width: '100%' }}
      onChange={setValue}
      suffixIcon={suffix}
      placeholder="Please select"
      options={[
        { value: 'Ava Swift', label: 'Ava Swift' },
        { value: 'Cole Reed', label: 'Cole Reed' },
        { value: 'Mia Blake', label: 'Mia Blake' },
        { value: 'Jake Stone', label: 'Jake Stone' },
        { value: 'Lily Lane', label: 'Lily Lane' },
        { value: 'Ryan Chase', label: 'Ryan Chase' },
        { value: 'Zoe Fox', label: 'Zoe Fox' },
        { value: 'Alex Grey', label: 'Alex Grey' },
        { value: 'Elle Blair', label: 'Elle Blair' },
      ]}
    />
  );
};

export default App;
```
