## zh-CN

使用 `size` 设置元素之间的间距，预设了 `small`、`middle`、`large` 三种尺寸，也可以自定义间距，若不设置 `size`，则默认为 `small`。

## en-US

Use `size` to set the spacing, Three sizes are preset: `small`, `middle`, `large`. You can also customize the spacing. If `size` is not set, the spacing is `small`.
```tsx
import React, { useState } from 'react';
import { Button, Radio, Slider, Space } from 'antd';
import type { ConfigProviderProps } from 'antd';

type SizeType = ConfigProviderProps['componentSize'];

const App: React.FC = () => {
  const [size, setSize] = useState<SizeType | [SizeType, SizeType] | 'customize'>('small');
  const [customSize, setCustomSize] = React.useState<number>(0);
  return (
    <>
      <Radio.Group value={size} onChange={(e) => setSize(e.target.value)}>
        {['small', 'middle', 'large', 'customize'].map((item) => (
          <Radio key={item} value={item}>
            {item}
          </Radio>
        ))}
      </Radio.Group>
      <br />
      <br />
      {size === 'customize' && (
        <>
          <Slider value={customSize} onChange={setCustomSize} />
          <br />
        </>
      )}
      <Space size={size !== 'customize' ? size : customSize}>
        <Button type="primary">Primary</Button>
        <Button>Default</Button>
        <Button type="dashed">Dashed</Button>
        <Button type="link">Link</Button>
      </Space>
    </>
  );
};

export default App;
```
