#
# PySNMP MIB module CISCO-POWER-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POWER-ETHERNET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPowerEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 412))
ciscoPowerEthernetCapability.setRevisions(('2012-09-04 00:00', '2012-04-06 00:00', '2009-02-14 00:00', '2007-07-09 00:00', '2007-02-08 00:00', '2006-05-31 00:00', '2004-06-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setRevisionsDescriptions(('Added capability statement\n        cPowerEthernetCapV15RO101SYPCat6K.', 'Added capability statement \n        cPowerEthernetCapV12RO233SXJ2PCat6K.\n         \n        Modified VARIATION of pethPsePortPowerPairs in \n        cPowerEthernetCapV12RO233SXHPCat6K.\n\n        Removed VARIATION of pethPsePortPowerPairsControlAbility \n        from cPowerEthernetCapCatOSV08R0401 and \n        cPowerEthernetCapV12RO233SXHPCat6K.', 'Added capability statement\n        cPowerEthernetCapV12RO252SGPCat4K.', 'Added capability statement\n        cPowerEthernetCapV12RO233SXHPCat6K.', 'Added a new AGENT-CAPABILITIES cPowerEthernetCapC3kV122SR035 for\n        c3550', 'Added the VARIATION for\n        pethPsePortPowerPriority in \n        cPowerEthernetCapCatOSV08R0401.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setContactInfo('       Cisco Systems\n                    Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setDescription('The capabilities description of\n        POWER-ETHERNET-MIB.')
cPowerEthernetCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapCatOSV08R0401 = cPowerEthernetCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapCatOSV08R0401 = cPowerEthernetCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapCatOSV08R0401.setDescription('POWER-ETHERNET-MIB capabilities.')
cPowerEthernetCapC3kV122SR035 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapC3kV122SR035 = cPowerEthernetCapC3kV122SR035.setProductRelease('CISCO IOS 12.2S(0.35) for cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapC3kV122SR035 = cPowerEthernetCapC3kV122SR035.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapC3kV122SR035.setDescription('POWER-ETHERNET-MIB Capabilities')
cPowerEthernetCapV12RO233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXHPCat6K = cPowerEthernetCapV12RO233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXHPCat6K = cPowerEthernetCapV12RO233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapV12RO233SXHPCat6K.setDescription('POWER-ETHERNET-MIB capabilities.')
cPowerEthernetCapV12RO252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO252SGPCat4K = cPowerEthernetCapV12RO252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO252SGPCat4K = cPowerEthernetCapV12RO252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapV12RO252SGPCat4K.setDescription('POWER-ETHERNET-MIB capabilities.')
cPowerEthernetCapV12RO233SXJ2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXJ2PCat6K = cPowerEthernetCapV12RO233SXJ2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXJ2PCat6K = cPowerEthernetCapV12RO233SXJ2PCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapV12RO233SXJ2PCat6K.setDescription('POWER-ETHERNET-MIB capabilities.')
cPowerEthernetCapV15RO101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV15RO101SYPCat6K = cPowerEthernetCapV15RO101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV15RO101SYPCat6K = cPowerEthernetCapV15RO101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthernetCapV15RO101SYPCat6K.setDescription('POWER-ETHERNET-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-CAPABILITY", cPowerEthernetCapCatOSV08R0401=cPowerEthernetCapCatOSV08R0401, cPowerEthernetCapV15RO101SYPCat6K=cPowerEthernetCapV15RO101SYPCat6K, PYSNMP_MODULE_ID=ciscoPowerEthernetCapability, cPowerEthernetCapC3kV122SR035=cPowerEthernetCapC3kV122SR035, cPowerEthernetCapV12RO233SXJ2PCat6K=cPowerEthernetCapV12RO233SXJ2PCat6K, cPowerEthernetCapV12RO252SGPCat4K=cPowerEthernetCapV12RO252SGPCat4K, ciscoPowerEthernetCapability=ciscoPowerEthernetCapability, cPowerEthernetCapV12RO233SXHPCat6K=cPowerEthernetCapV12RO233SXHPCat6K)
