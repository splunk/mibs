#
# PySNMP MIB module CISCO-HW-MODULE-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HW-MODULE-CONTROL-CAPABILITY
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
ciscoHwModuleControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 588))
ciscoHwModuleControlCapability.setRevisions(('2012-09-07 00:00', '2011-09-27 00:00', '2010-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setRevisionsDescriptions(('Added capability statement chmcCapV15R0001SY1PCat6K.', 'Added capability statement chmcCapV15R0001SYPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setDescription('Agent capabilities for CISCO-HW-MODULE-CONTROL-MIB.')
chmcCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: chmcCapV12R0233SXI4PCat6K.setDescription('CISCO-HW-MODULE-CONTROL-MIB agent capabilities.')
chmcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: chmcCapV15R0001SYPCat6K.setDescription('CISCO-HW-MODULE-CONTROL-MIB agent capabilities.')
chmcCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setStatus('current')
if mibBuilder.loadTexts: chmcCapV15R0001SY1PCat6K.setDescription('CISCO-HW-MODULE-CONTROL-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-HW-MODULE-CONTROL-CAPABILITY", chmcCapV15R0001SYPCat6K=chmcCapV15R0001SYPCat6K, ciscoHwModuleControlCapability=ciscoHwModuleControlCapability, chmcCapV12R0233SXI4PCat6K=chmcCapV12R0233SXI4PCat6K, PYSNMP_MODULE_ID=ciscoHwModuleControlCapability, chmcCapV15R0001SY1PCat6K=chmcCapV15R0001SY1PCat6K)
