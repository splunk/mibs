#
# PySNMP MIB module CISCO-AAA-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SERVER-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAAAServerExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 372))
ciscoAAAServerExtCapability.setRevisions(('2008-06-16 00:00', '2006-02-21 00:00', '2004-08-24 00:00', '2003-11-22 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setLastUpdated('200806160000Z')
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoAAAServerExtCapMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setStatus('current')
ciscoAAAServerExtCapMDS20R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setProductRelease('Cisco MDS 2.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setStatus('current')
ciscoAAAServerExtCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setStatus('current')
ciscoAAAServerExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                        for ACE 4710 Application Control Engine \n                        Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-EXT-CAPABILITY", ciscoAAAServerExtCapability=ciscoAAAServerExtCapability, PYSNMP_MODULE_ID=ciscoAAAServerExtCapability, ciscoAAAServerExtCapc4710aceVA1R700=ciscoAAAServerExtCapc4710aceVA1R700, ciscoAAAServerExtCapACSWV03R000=ciscoAAAServerExtCapACSWV03R000, ciscoAAAServerExtCapMDS13R1=ciscoAAAServerExtCapMDS13R1, ciscoAAAServerExtCapMDS20R1=ciscoAAAServerExtCapMDS20R1)
