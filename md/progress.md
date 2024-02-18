---
category: Components
subtitle: 进度条
group: 反馈
title: Progress
cover: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*gK_4S6fDRfgAAAAAAAAAAAAADrJ8AQ/original
coverDark: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*HJH8Tb1lcYAAAAAAAAAAAAAADrJ8AQ/original
demo:
  cols: 2
---

展示操作的当前进度。

## 何时使用

在操作需要较长时间才能完成时，为用户显示该操作的当前进度和状态。

- 当一个操作会打断当前界面，或者需要在后台运行，且耗时可能超过 2 秒时；
- 当需要显示一个操作完成的百分比时。

## 代码演示

<!-- prettier-ignore -->
<code src="./demo/line.tsx">进度条</code>
<code src="./demo/circle.tsx">进度圈</code>
<code src="./demo/line-mini.tsx">小型进度条</code>
<code src="./demo/circle-micro.tsx">响应式进度圈</code>
<code src="./demo/circle-mini.tsx">小型进度圈</code>
<code src="./demo/dynamic.tsx">动态展示</code>
<code src="./demo/format.tsx">自定义文字格式</code>
<code src="./demo/dashboard.tsx">仪表盘</code>
<code src="./demo/segment.tsx">分段进度条</code>
<code src="./demo/linecap.tsx">边缘形状</code>
<code src="./demo/gradient-line.tsx">自定义进度条渐变色</code>
<code src="./demo/steps.tsx">步骤进度条</code>
<code src="./demo/size.tsx">尺寸</code>

## API

通用属性参考：[通用属性](/docs/react/common-props)

各类型共用的属性。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| format | 内容的模板函数 | function(percent, successPercent) | (percent) => percent + `%` | - |
| percent | 百分比 | number | 0 | - |
| showInfo | 是否显示进度数值或状态图标 | boolean | true | - |
| status | 状态，可选：`success` `exception` `normal` `active`(仅限 line) | string | - | - |
| strokeColor | 进度条的色彩 | string | - | - |
| strokeLinecap | 进度条的样式 | `round` \| `butt` \| `square`，区别详见 [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap) | `round` | - |
| success | 成功进度条相关配置 | { percent: number, strokeColor: string } | - | - |
| trailColor | 未完成的分段的颜色 | string | - | - |
| type | 类型，可选 `line` `circle` `dashboard` | string | `line` | - |
| size | 进度条的尺寸 | number \| \[number \| string, number] \| "small" \| "default" | "default" | v5.3.0 |

### `type="line"`

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| steps | 进度条总共步数 | number | - | - |
| strokeColor | 进度条的色彩，传入 object 时为渐变。当有 `steps` 时支持传入一个数组。 | string \| string[] \| { from: string; to: string; direction: string } | - | 4.21.0: `string[]` |

### `type="circle"`

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| strokeColor | 圆形进度条线的色彩，传入 object 时为渐变 | string \| { number%: string } | - | - |
| strokeWidth | 圆形进度条线的宽度，单位是进度条画布宽度的百分比 | number | 6 | - |

### `type="dashboard"`

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| gapDegree | 仪表盘进度条缺口角度，可取值 0 ~ 295 | number | 75 | - |
| gapPosition | 仪表盘进度条缺口位置 | `top` \| `bottom` \| `left` \| `right` | `bottom` | - |
| strokeWidth | 仪表盘进度条线的宽度，单位是进度条画布宽度的百分比 | number | 6 | - |

## 主题变量（Design Token）

<ComponentTokenTable component="Progress"></ComponentTokenTable>

## steps demo
>/demo/steps.tsx


带步骤的进度条。



A progress bar with steps.
```tsx
import React from 'react';
import { red, green } from '@ant-design/colors';
import { Progress } from 'antd';

const App: React.FC = () => (
  <>
    <Progress percent={50} steps={3} />
    <br />
    <Progress percent={30} steps={5} />
    <br />
    <Progress percent={100} steps={5} size="small" strokeColor={green[6]} />
    <br />
    <Progress percent={60} steps={5} strokeColor={[green[6], green[6], red[5]]} />
  </>
);

export default App;
```

## size demo
>/demo/size.tsx


进度条尺寸。



The size of progress.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <>
    <Space direction="vertical">
      <Progress percent={50} />
      <Progress percent={50} size="small" />
      <Progress percent={50} size={[300, 20]} />
    </Space>
    <br />
    <br />
    <Space size={30}>
      <Progress type="circle" percent={50} />
      <Progress type="circle" percent={50} size="small" />
      <Progress type="circle" percent={50} size={20} />
    </Space>
    <br />
    <br />
    <Space size={30}>
      <Progress type="dashboard" percent={50} />
      <Progress type="dashboard" percent={50} size="small" />
      <Progress type="dashboard" percent={50} size={20} />
    </Space>
    <br />
    <br />
    <Space size={30} wrap>
      <Progress steps={3} percent={50} />
      <Progress steps={3} percent={50} size="small" />
      <Progress steps={3} percent={50} size={20} />
      <Progress steps={3} percent={50} size={[20, 30]} />
    </Space>
  </>
);

export default App;
```

## dashboard demo
>/demo/dashboard.tsx


通过设置 `type=dashboard`，可以很方便地实现仪表盘样式的进度条。若想要修改缺口的角度，可以设置 `gapDegree` 为你想要的值。



By setting `type=dashboard`, you can get a dashboard style of progress easily. Modify `gapDegree` to set the degree of gap.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="dashboard" percent={75} />
    <Progress type="dashboard" percent={75} gapDegree={30} />
  </Space>
);

export default App;
```

## segment demo
>/demo/segment.tsx


分段展示进度，可以用于细化进度语义。



Show several parts of progress with different status.
```tsx
import React from 'react';
import { Progress, Tooltip, Space } from 'antd';

const App: React.FC = () => (
  <>
    <Tooltip title="3 done / 3 in progress / 4 to do">
      <Progress percent={60} success={{ percent: 30 }} />
    </Tooltip>
    <Space wrap>
      <Tooltip title="3 done / 3 in progress / 4 to do">
        <Progress percent={60} success={{ percent: 30 }} type="circle" />
      </Tooltip>
      <Tooltip title="3 done / 3 in progress / 4 to do">
        <Progress percent={60} success={{ percent: 30 }} type="dashboard" />
      </Tooltip>
    </Space>
  </>
);

export default App;
```

## circle-mini demo
>/demo/circle-mini.tsx


小一号的圈形进度。



A smaller circular progress bar.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="circle" percent={30} size={80} />
    <Progress type="circle" percent={70} size={80} status="exception" />
    <Progress type="circle" percent={100} size={80} />
  </Space>
);

export default App;
```

## circle demo
>/demo/circle.tsx


圈形的进度。



A circular progress bar.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="circle" percent={75} />
    <Progress type="circle" percent={70} status="exception" />
    <Progress type="circle" percent={100} />
  </Space>
);

export default App;
```

## gradient-line demo
>/demo/gradient-line.tsx


渐变色封装，`circle` 与 `dashboard` 设置渐变时 `strokeLinecap` 会被忽略。



Gradient encapsulation, `circle` and `dashboard` will ignore `strokeLinecap` when setting gradient.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const twoColors = { '0%': '#108ee9', '100%': '#87d068' };
const conicColors = { '0%': '#87d068', '50%': '#ffe58f', '100%': '#ffccc7' };

const App: React.FC = () => (
  <div style={{ display: 'flex', flexDirection: 'column', rowGap: 16 }}>
    <Progress percent={99.9} strokeColor={twoColors} />
    <Progress percent={50} status="active" strokeColor={{ from: '#108ee9', to: '#87d068' }} />
    <Space wrap>
      <Progress type="circle" percent={90} strokeColor={twoColors} />
      <Progress type="circle" percent={100} strokeColor={twoColors} />
      <Progress type="circle" percent={93} strokeColor={conicColors} />
    </Space>
    <Space wrap>
      <Progress type="dashboard" percent={90} strokeColor={twoColors} />
      <Progress type="dashboard" percent={100} strokeColor={twoColors} />
      <Progress type="dashboard" percent={93} strokeColor={conicColors} />
    </Space>
  </div>
);

export default App;
```

## component-token demo
>/demo/component-token.tsx


组件 Token Debug.



Component Token Debug.
```tsx
import React from 'react';
import { ConfigProvider, Progress, Space } from 'antd';

const App: React.FC = () => (
  <ConfigProvider
    theme={{
      token: {
        marginXXS: 20,
        fontSizeSM: 24,
      },
      components: {
        Progress: {
          defaultColor: '#bae0ff',
          remainingColor: '#f5222d',
          colorText: '#52c41a',
          circleTextColor: '#52c41a',
          lineBorderRadius: 50,
        },
      },
    }}
  >
    <Space direction="vertical">
      <Progress percent={50} />
      <Progress percent={50} size="small" />
      <Progress percent={50} size={[300, 20]} />
    </Space>
    <br />
    <br />
    <Space size={30}>
      <Progress type="circle" percent={50} />
      <Progress type="circle" percent={50} size="small" />
      <Progress type="circle" percent={50} size={20} />
    </Space>
    <br />
    <br />
    <Space size={30}>
      <Progress type="dashboard" percent={50} />
      <Progress type="dashboard" percent={50} size="small" />
      <Progress type="dashboard" percent={50} size={20} />
    </Space>
    <br />
    <br />
    <Space size={30} wrap>
      <Progress steps={3} percent={50} />
      <Progress steps={3} percent={50} size="small" />
      <Progress steps={3} percent={50} size={20} />
      <Progress steps={3} percent={50} size={[20, 30]} />
    </Space>
  </ConfigProvider>
);

export default App;
```

## dynamic demo
>/demo/dynamic.tsx


会动的进度条才是好进度条。



A dynamic progress bar is better.
```tsx
import React, { useState } from 'react';
import { MinusOutlined, PlusOutlined } from '@ant-design/icons';
import { Button, Progress } from 'antd';

const App: React.FC = () => {
  const [percent, setPercent] = useState<number>(0);

  const increase = () => {
    setPercent((prevPercent) => {
      const newPercent = prevPercent + 10;
      if (newPercent > 100) {
        return 100;
      }
      return newPercent;
    });
  };

  const decline = () => {
    setPercent((prevPercent) => {
      const newPercent = prevPercent - 10;
      if (newPercent < 0) {
        return 0;
      }
      return newPercent;
    });
  };

  return (
    <>
      <div style={{ marginBottom: 10 }}>
        <Progress percent={percent} />
        <Progress type="circle" percent={percent} />
      </div>
      <Button.Group>
        <Button onClick={decline} icon={<MinusOutlined />} />
        <Button onClick={increase} icon={<PlusOutlined />} />
      </Button.Group>
    </>
  );
};

export default App;
```

## circle-micro demo
>/demo/circle-micro.tsx


响应式的圈形进度，当 `width` 小于等于 20 的时候，进度信息将不会显示在进度圈里面，而是以 Tooltip 的形式显示。



Responsive circular progress bar. When `width` is smaller than 20, progress information will be displayed in Tooltip.
```tsx
import React from 'react';
import { Progress } from 'antd';

const App: React.FC = () => (
  <>
    <Progress
      type="circle"
      trailColor="#e6f4ff"
      percent={60}
      strokeWidth={20}
      size={14}
      format={(number) => `进行中，已完成${number}%`}
    />
    <span style={{ marginLeft: 8 }}>代码发布</span>
  </>
);

export default App;
```

## linecap demo
>/demo/linecap.tsx


通过设定 `strokeLinecap="butt"` 可以调整进度条边缘的形状为方形，详见 [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap)。



By setting `strokeLinecap="butt"`, you can change the linecaps from `round` to `butt`, see [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap) for more information.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <>
    <Progress strokeLinecap="butt" percent={75} />
    <Space wrap>
      <Progress strokeLinecap="butt" type="circle" percent={75} />
      <Progress strokeLinecap="butt" type="dashboard" percent={75} />
    </Space>
  </>
);

export default App;
```

## line-mini demo
>/demo/line-mini.tsx


适合放在较狭窄的区域内。



Appropriate for a narrow area.
```tsx
import React from 'react';
import { Progress } from 'antd';

const App: React.FC = () => (
  <div style={{ width: 170 }}>
    <Progress percent={30} size="small" />
    <Progress percent={50} size="small" status="active" />
    <Progress percent={70} size="small" status="exception" />
    <Progress percent={100} size="small" />
  </div>
);

export default App;
```

## format demo
>/demo/format.tsx


`format` 属性指定格式。



You can set a custom text by setting the `format` prop.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="circle" percent={75} format={(percent) => `${percent} Days`} />
    <Progress type="circle" percent={100} format={() => 'Done'} />
  </Space>
);

export default App;
```

## line demo
>/demo/line.tsx


标准的进度条。



A standard progress bar.
```tsx
import React from 'react';
import { Progress } from 'antd';

const App: React.FC = () => (
  <>
    <Progress percent={30} />
    <Progress percent={50} status="active" />
    <Progress percent={70} status="exception" />
    <Progress percent={100} />
    <Progress percent={50} showInfo={false} />
  </>
);

export default App;
```
