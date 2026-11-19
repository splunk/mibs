#
# PySNMP MIB module CISCO-APPLICATION-ACCELERATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-APPLICATION-ACCELERATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppAccCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 567))
ciscoAppAccCapability.setRevisions(('2008-07-29 00:00',))
if mibBuilder.loadTexts: ciscoAppAccCapability.setLastUpdated('200807290000Z')
if mibBuilder.loadTexts: ciscoAppAccCapability.setOrganization('Cisco Systems, Inc.')
ciscoAppAccCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 567, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for ACE \n                4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPLICATION-ACCELERATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppAccCapability, ciscoAppAccCapc4710aceVA1R700=ciscoAppAccCapc4710aceVA1R700, ciscoAppAccCapability=ciscoAppAccCapability)
