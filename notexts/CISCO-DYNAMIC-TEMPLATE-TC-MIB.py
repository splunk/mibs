#
# PySNMP MIB module CISCO-DYNAMIC-TEMPLATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DYNAMIC-TEMPLATE-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDynamicTemplateTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 783))
ciscoDynamicTemplateTcMIB.setRevisions(('2007-09-06 00:00',))
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setLastUpdated('201201270000Z')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setOrganization('Cisco Systems, Inc.')
class DynamicTemplateName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class DynamicTemplateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("derived", 2), ("ppp", 3), ("ethernet", 4), ("ipSubscriber", 5), ("service", 6))

class DynamicTemplateTargetType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("interface", 2))

class DynamicTemplateTargetId(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

mibBuilder.exportSymbols("CISCO-DYNAMIC-TEMPLATE-TC-MIB", DynamicTemplateType=DynamicTemplateType, DynamicTemplateTargetId=DynamicTemplateTargetId, ciscoDynamicTemplateTcMIB=ciscoDynamicTemplateTcMIB, DynamicTemplateName=DynamicTemplateName, PYSNMP_MODULE_ID=ciscoDynamicTemplateTcMIB, DynamicTemplateTargetType=DynamicTemplateTargetType)
