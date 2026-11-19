#
# PySNMP MIB module CISCO-AAA-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SERVER-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAAAServerExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 372))
ciscoAAAServerExtCapability.setRevisions(('2008-06-16 00:00', '2006-02-21 00:00', '2004-08-24 00:00', '2003-11-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setRevisionsDescriptions(('Agent capabilities for Cisco ACE 4710 Application\n        Control Engine Appliance.', 'Agent capabilities for Cisco\n        Application Control Engine (ACE).', 'Agent capabilities for Cisco MDS 2.0.', 'Agent capabilities for Cisco MDS 1.3.',))
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setLastUpdated('200806160000Z')
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setDescription('Agent capabilities for CISCO-AAA-SERVER-EXT-MIB')
ciscoAAAServerExtCapMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerExtCapMDS13R1.setDescription('Cisco AAA Server MIB capabilities')
ciscoAAAServerExtCapMDS20R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setProductRelease('Cisco MDS 2.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerExtCapMDS20R1.setDescription('Cisco AAA Server MIB capabilities')
ciscoAAAServerExtCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerExtCapACSWV03R000.setDescription('Cisco AAA Server MIB capabilities')
ciscoAAAServerExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                        for ACE 4710 Application Control Engine \n                        Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerExtCapc4710aceVA1R700.setDescription('Cisco AAA Server MIB capabilities')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-EXT-CAPABILITY", ciscoAAAServerExtCapability=ciscoAAAServerExtCapability, ciscoAAAServerExtCapACSWV03R000=ciscoAAAServerExtCapACSWV03R000, PYSNMP_MODULE_ID=ciscoAAAServerExtCapability, ciscoAAAServerExtCapc4710aceVA1R700=ciscoAAAServerExtCapc4710aceVA1R700, ciscoAAAServerExtCapMDS20R1=ciscoAAAServerExtCapMDS20R1, ciscoAAAServerExtCapMDS13R1=ciscoAAAServerExtCapMDS13R1)
