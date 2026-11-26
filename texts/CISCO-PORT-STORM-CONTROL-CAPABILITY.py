#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-STORM-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
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
ciscoPortStormControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 542))
ciscoPortStormControlCapability.setRevisions(('2014-04-04 00:00', '2012-09-07 00:00', '2011-03-24 00:00', '2007-07-03 00:00', '2007-07-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortStormControlCapability.setRevisionsDescriptions(('Added capability statement cpscCapabilityV06R0002U0301PN3K.', 'Added capability statement cpscCapabilityV15R0101SYPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXJPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n            Tel: +1 800 553-NETS \n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setDescription('Agent capabilities for CISCO-PORT-STORM-CONTROL-MIB.')
cpscCapabilityV12R0240SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setProductRelease('Cisco IOS 12.2(40)SG on Cat4K platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0240SGCat4K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities')
cpscCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXHPCat6K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXJPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV15R0101SYPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV06R0002U0301PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setProductRelease('Cisco NX-OS 6.0(2)U3(1) on Nexus 3000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV06R0002U0301PN3K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-CAPABILITY", cpscCapabilityV12R0233SXHPCat6K=cpscCapabilityV12R0233SXHPCat6K, cpscCapabilityV15R0101SYPCat6k=cpscCapabilityV15R0101SYPCat6k, ciscoPortStormControlCapability=ciscoPortStormControlCapability, cpscCapabilityV12R0240SGCat4K=cpscCapabilityV12R0240SGCat4K, cpscCapabilityV06R0002U0301PN3K=cpscCapabilityV06R0002U0301PN3K, cpscCapabilityV12R0233SXJPCat6k=cpscCapabilityV12R0233SXJPCat6k, PYSNMP_MODULE_ID=ciscoPortStormControlCapability)
