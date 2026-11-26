#
# PySNMP MIB module CISCO-IEEE8021-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8021-CFM-CAPABILITY
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
ciscoIeee8021CfmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 578))
ciscoIeee8021CfmCapability.setRevisions(('2010-02-23 00:00', '2009-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoIeee8021CfmCapV12R0254SE.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setLastUpdated('201002230000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA 95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setDescription('The capabilities description of IEEE8021-CFM-MIB.')
ciscoIeee8021CfmCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapCatOSV08R0702.setDescription('IEEE8021-CFM-MIB capabilities.')
ciscoIeee8021CfmCapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapV12R0254SE.setDescription('IEEE8021-CFM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021CfmCapability, ciscoIeee8021CfmCapability=ciscoIeee8021CfmCapability, ciscoIeee8021CfmCapCatOSV08R0702=ciscoIeee8021CfmCapCatOSV08R0702, ciscoIeee8021CfmCapV12R0254SE=ciscoIeee8021CfmCapV12R0254SE)
